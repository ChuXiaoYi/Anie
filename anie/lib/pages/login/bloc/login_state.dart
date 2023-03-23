part of 'login_bloc.dart';

abstract class LoginState extends Equatable {
  const LoginState();

  @override
  List<Object> get props => [];
}

class LoginInitial extends LoginState {
  const LoginInitial(
      {this.status = FormzStatus.pure,
      this.username = const Username.pure(),
      this.password = const Password.pure()});

  final FormzStatus status;
  final Username username;
  final Password password;

  LoginInitial copyWith({
    FormzStatus? status,
    Username? username,
    Password? password,
  }) {
    return LoginInitial(
      status: status ?? this.status,
      username: username ?? this.username,
      password: password ?? this.password,
    );
  }

  @override
  List<Object> get props => [status, username, password];
}
