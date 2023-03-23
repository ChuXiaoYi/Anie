// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables

import 'package:anie/api/authentication/authentication_repository.dart';
import 'package:anie/pages/login/bloc/login_bloc.dart';
import 'package:anie/pages/login/view/login_form.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  static Route route() {
    return MaterialPageRoute<void>(builder: (_) => const LoginPage());
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Padding(
            padding: const EdgeInsets.all(12),
            child: SafeArea(
              child: Container(
                margin: EdgeInsets.only(top: 100),
                child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        "Hi, 欢迎回来!",
                        style: TextStyle(
                            fontSize: 30,
                            fontWeight: FontWeight.bold,
                            color: Colors.black),
                      ),
                      BlocProvider(
                        create: (context) => LoginBloc(
                          authenticationRepository:
                              RepositoryProvider.of<AuthenticationRepository>(
                                  context),
                        ),
                        child: const LoginForm(),
                      ),
                      const Spacer(),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Text("还没有账户? "),
                          TextButton(
                              onPressed: () {},
                              child: Text(
                                "注册",
                                style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                    decoration: TextDecoration.underline),
                              ))
                        ],
                      )
                    ]),
              ),
            )));
  }
}
