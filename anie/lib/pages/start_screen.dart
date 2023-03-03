import 'package:flutter/material.dart';

class StartScreen extends StatefulWidget {
  // final String title;

  const StartScreen({super.key});

  @override
  State<StartScreen> createState() => _StartScreenState();
}

class _StartScreenState extends State<StartScreen> {
  @override
  Widget build(BuildContext context) {
    return Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment(0.8, 1),
              colors: <Color>[
                Color.fromRGBO(155, 108, 220, 1),
                Color.fromRGBO(249, 247, 247, 1),
              ]),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Container(
              margin: const EdgeInsets.only(top: 121),
              alignment: Alignment.center,
              decoration: const BoxDecoration(
                  borderRadius: BorderRadius.vertical(
                      top: Radius.circular(200), bottom: Radius.circular(30)),
                  image: DecorationImage(
                      image: AssetImage(
                    'assets/images/start_screen01.png',
                  ))),
              width: 250,
              height: 394,
            ),
            Container(
              width: 268,
              height: 29,
              margin: const EdgeInsets.only(top: 40),
              child: const Text(
                'Find your new friends',
                style: TextStyle(
                    fontSize: 24,
                    fontFamily: 'Poppins',
                    fontWeight: FontWeight.w700,
                    letterSpacing: 0.01,
                    color: Color.fromRGBO(95, 91, 91, 1),
                    decoration: TextDecoration.none),
              ),
            ),
            Container(
              width: 285,
              height: 36,
              margin: const EdgeInsets.only(top: 16),
              child: const Text(
                'Make your life more happy with us to have a little new friends',
                textAlign: TextAlign.center,
                style: TextStyle(
                    fontSize: 14,
                    fontFamily: 'Poppins',
                    fontWeight: FontWeight.w400,
                    color: Color.fromRGBO(173, 168, 168, 1),
                    decoration: TextDecoration.none),
              ),
            ),
            Container(
              width: 273,
              height: 30,
              margin: const EdgeInsets.only(top: 33),
              child: OutlinedButton(
                style: OutlinedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(
                        vertical: 6.5, horizontal: 109),
                    shape: const RoundedRectangleBorder(
                        side: BorderSide(color: Color.fromRGBO(77, 0, 186, 1)),
                        borderRadius: BorderRadius.all(Radius.circular(8))),
                    backgroundColor: const Color.fromRGBO(77, 0, 186, 1)),
                child: const Text(
                  "Sign Up",
                  style: TextStyle(color: Colors.white),
                ),
                onPressed: () {
                  Navigator.pushNamed(context, "sign_up");
                },
              ),
            ),
            Container(
              width: 273,
              height: 30,
              margin: const EdgeInsets.only(top: 12),
              child: OutlinedButton(
                style: OutlinedButton.styleFrom(
                  shape: const RoundedRectangleBorder(
                      side: BorderSide(
                          color: Color.fromRGBO(77, 0, 186, 1), width: 01),
                      borderRadius: BorderRadius.all(Radius.circular(8))),
                ),
                child: const Text(
                  "Login",
                  style: TextStyle(color: Color.fromRGBO(77, 0, 186, 1)),
                ),
                onPressed: () {},
              ),
            ),
          ],
        ));
  }
}
