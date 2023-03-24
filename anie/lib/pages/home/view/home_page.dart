// ignore_for_file: prefer_const_constructors

import 'package:anie/pages/explore/explore.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:anie/authentication/authentication.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  static Route<void> route() {
    return MaterialPageRoute<void>(builder: (_) => const HomePage());
  }

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int currentPageIndex = 1;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: NavigationBar(
        onDestinationSelected: (int index) {
          setState(() {
            currentPageIndex = index;
          });
        },
        selectedIndex: currentPageIndex,
        destinations: const [
          NavigationDestination(
            icon: Icon(Icons.favorite),
            label: '关注',
          ),
          NavigationDestination(
            icon: Icon(Icons.home),
            label: '探索',
          ),
          NavigationDestination(
            icon: Icon(Icons.add_circle),
            label: '发布',
          ),
          NavigationDestination(
            icon: Icon(Icons.shopping_cart),
            label: '众筹',
          ),
          NavigationDestination(
            icon: Icon(Icons.person),
            label: '我的',
          ),
        ],
      ),
      body: Builder(builder: (context) {
        switch (currentPageIndex) {
          case 0:
            return const Center(child: Text('关注'));
          case 1:
            return const Explore();
          case 2:
            return const Center(child: Text('发布'));
          case 3:
            return const Center(child: Text('众筹'));
          case 4:
            return const Center(child: Text('我的'));
          default:
            return const Center(child: Text('探索'));
        }
      }),
    );
  }
}
