import 'dart:async';
import 'package:anie/common/net/dio_utils.dart';

enum AuthenticationStatus { unknown, authenticated, unauthenticated }

class AuthenticationRepository {
  final _controller = StreamController<AuthenticationStatus>();

  Stream<AuthenticationStatus> get status async* {
    await Future<void>.delayed(const Duration(seconds: 1));
    yield AuthenticationStatus.unauthenticated;
    yield* _controller.stream;
  }

  Future<void> logIn({
    required String username,
    required String password,
  }) async {
    HttpUtils.obj.upload('/token', params: {
      "username": username,
      "password": password,
    }).then((response) {
      HttpUtils.obj.dio.options.headers['Authorization'] =
          'Bearer ${response.data['access_token']}';
      _controller.add(AuthenticationStatus.authenticated);
    });
  }

  void logOut() {
    _controller.add(AuthenticationStatus.unauthenticated);
  }

  void dispose() => _controller.close();
}
