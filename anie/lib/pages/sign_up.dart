import 'package:flutter/material.dart';

class SignUpPage extends StatefulWidget {
  const SignUpPage({super.key});

  @override
  State<SignUpPage> createState() => _SignUpPageState();
}

class _SignUpPageState extends State<SignUpPage> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  bool _pwdShow = false;
  void onPressShowPwd() {
    setState(() {
      _pwdShow = !_pwdShow;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
          color: Colors.white,
          child: Column(children: [
            Container(
              alignment: Alignment.centerLeft,
              margin: const EdgeInsets.only(top: 145, left: 20),
              child: const Text(
                'Create account',
                style: TextStyle(
                    fontWeight: FontWeight.w700,
                    decoration: TextDecoration.none,
                    color: Color.fromRGBO(0, 0, 0, 1),
                    fontSize: 30,
                    fontFamily: 'Poppins'),
              ),
            ),
            Container(
                margin: const EdgeInsets.only(top: 38, left: 13, right: 13),
                child: Form(
                  key: _formKey,
                  child: Column(children: <Widget>[
                    Container(
                      margin: const EdgeInsets.only(top: 38),
                      child: TextFormField(
                        decoration: const InputDecoration(
                          enabledBorder: OutlineInputBorder(
                              borderRadius:
                                  BorderRadius.all(Radius.circular(10)),
                              borderSide: BorderSide(
                                  width: 1,
                                  color: Color.fromRGBO(216, 218, 220, 1))),
                          focusedBorder: OutlineInputBorder(
                              borderRadius:
                                  BorderRadius.all(Radius.circular(10)),
                              borderSide: BorderSide(
                                  width: 1,
                                  color: Color.fromRGBO(216, 218, 220, 1))),
                          hintText: 'Your username',
                          labelText: 'Username',
                          labelStyle: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 20,
                              color: Color.fromRGBO(0, 0, 0, 1)),
                          hintStyle: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 16,
                              color: Color.fromRGBO(0, 0, 0, 0.5)),
                        ),
                      ),
                    ),
                    Container(
                      margin: const EdgeInsets.only(top: 46),
                      child: TextFormField(
                        keyboardType: TextInputType.emailAddress,
                        decoration: const InputDecoration(
                          enabledBorder: OutlineInputBorder(
                              borderRadius:
                                  BorderRadius.all(Radius.circular(10)),
                              borderSide: BorderSide(
                                  width: 1,
                                  color: Color.fromRGBO(216, 218, 220, 1))),
                          focusedBorder: OutlineInputBorder(
                              borderRadius:
                                  BorderRadius.all(Radius.circular(10)),
                              borderSide: BorderSide(
                                  width: 1,
                                  color: Color.fromRGBO(216, 218, 220, 1))),
                          hintText: 'Your email',
                          labelText: 'Email',
                          labelStyle: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 20,
                              color: Color.fromRGBO(0, 0, 0, 1)),
                          hintStyle: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 16,
                              color: Color.fromRGBO(0, 0, 0, 0.5)),
                        ),
                      ),
                    ),
                    Container(
                      margin: const EdgeInsets.only(top: 46),
                      child: TextFormField(
                          obscureText: !_pwdShow,
                          decoration: const InputDecoration(
                            enabledBorder: OutlineInputBorder(
                                borderRadius:
                                    BorderRadius.all(Radius.circular(10)),
                                borderSide: BorderSide(
                                    width: 1,
                                    color: Color.fromRGBO(216, 218, 220, 1))),
                            focusedBorder: OutlineInputBorder(
                                borderRadius:
                                    BorderRadius.all(Radius.circular(10)),
                                borderSide: BorderSide(
                                    width: 1,
                                    color: Color.fromRGBO(216, 218, 220, 1))),
                            hintText: 'Your email',
                            labelText: 'Password',
                            labelStyle: TextStyle(
                                fontWeight: FontWeight.w400,
                                fontSize: 20,
                                color: Color.fromRGBO(0, 0, 0, 1)),
                            hintStyle: TextStyle(
                                fontWeight: FontWeight.w400,
                                fontSize: 16,
                                color: Color.fromRGBO(0, 0, 0, 0.5)),
                          )),
                    ),
                    Container(
                      margin: const EdgeInsets.only(top: 25),
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        mainAxisAlignment: MainAxisAlignment.start,
                        children: const [
                          Icon(Icons.check_circle),
                          Padding(
                            padding: EdgeInsets.all(8.0),
                            child:
                                Text('I accept the terms and privacy policy'),
                          )
                        ],
                      ),
                    ),
                    Container(
                      width: 353,
                      height: 40,
                      margin: const EdgeInsets.only(top: 53),
                      child: OutlinedButton(
                        style: OutlinedButton.styleFrom(
                            padding: const EdgeInsets.symmetric(
                                vertical: 6.5, horizontal: 109),
                            shape: const RoundedRectangleBorder(
                                side: BorderSide(
                                    color: Color.fromRGBO(77, 0, 186, 1)),
                                borderRadius:
                                    BorderRadius.all(Radius.circular(8))),
                            backgroundColor:
                                const Color.fromRGBO(77, 0, 186, 1)),
                        child: const Text(
                          "Sign Up",
                          style: TextStyle(color: Colors.white),
                        ),
                        onPressed: () {
                          // Navigator.pushNamed(context, "sign_up");
                          print("go to /");
                        },
                      ),
                    )
                  ]),
                )),
            Container(
              margin: const EdgeInsets.only(top: 124),
              alignment: Alignment.center,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text("Already have an account?"),
                  TextButton(
                    child: const Text("Log in"),
                    onPressed: () => Navigator.pushNamed(context, 'login'),
                  )
                ],
              ),
            )
          ])),
    );
  }
}
