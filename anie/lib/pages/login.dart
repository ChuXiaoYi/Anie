import 'package:flutter/material.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginState();
}

class _LoginState extends State<LoginPage> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  bool _pwdShow = false;
  void onPressShowPwd() {
    setState(() {
      _pwdShow = !_pwdShow;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
    );
  }
}
