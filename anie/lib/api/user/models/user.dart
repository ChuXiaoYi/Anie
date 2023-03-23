import 'package:equatable/equatable.dart';

class User extends Equatable {
  const User(
      {required this.id,
      required this.username,
      required this.phone,
      required this.status});

  final int id;
  final String username;
  final String phone;
  final int status;

  @override
  List<Object> get props => [id];

  static const empty = User(id: 0, username: '', phone: '', status: 0);

  User.fromJson(Map<String, dynamic> json)
      : id = json['id'],
        username = json['username'],
        phone = json['phone'],
        status = json['status'];
}
