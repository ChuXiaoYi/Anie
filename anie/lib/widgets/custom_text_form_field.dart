import 'package:flutter/material.dart';

class CustomTextFormField extends StatelessWidget {
  const CustomTextFormField({super.key});

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      decoration: const InputDecoration(
        enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.all(Radius.circular(10)),
            borderSide:
                BorderSide(width: 1, color: Color.fromRGBO(216, 218, 220, 1))),
        focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.all(Radius.circular(10)),
            borderSide:
                BorderSide(width: 1, color: Color.fromRGBO(216, 218, 220, 1))),
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
    );
  }
}
