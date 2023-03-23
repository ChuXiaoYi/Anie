import 'package:anie/common/net/base_res.dart';
import 'package:anie/common/net/dio_utils.dart';
import 'package:uuid/uuid.dart';

import 'models/models.dart';

class UserRepository {
  User? _user;

  Future<User?> getUser() async {
    if (_user != null) return _user;
    BaseResponse response = await HttpUtils.obj.post('/current_user');

    return User.fromJson(response.data);
  }
}
