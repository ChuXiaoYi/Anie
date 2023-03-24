// ignore_for_file: prefer_const_constructors

import 'package:anie/components/searchbar.dart';
import 'package:flutter/material.dart';

class Explore extends StatefulWidget {
  const Explore({super.key});

  @override
  State<Explore> createState() => _ExploreState();
}

class _ExploreState extends State<Explore> {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Padding(
        padding: const EdgeInsets.all(14.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const SearchBar(),
            AnimalCategoryWidget(),
            const SizedBox(height: 14),
            Expanded(child: InfiniteGridView()),
          ],
        ),
      ),
    );
  }
}

class AnimalCategoryWidget extends StatefulWidget {
  const AnimalCategoryWidget({
    super.key,
  });

  @override
  State<AnimalCategoryWidget> createState() => _AnimalCategoryWidgetState();
}

class _AnimalCategoryWidgetState extends State<AnimalCategoryWidget> {
  int selectedCategory = 0;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(top: 14),
      child: Row(
        children: [
          Expanded(
            child: FilledButton.icon(
              onPressed: () {},
              label: const Text('猫猫', style: TextStyle(fontSize: 12)),
              icon: const Icon(Icons.pets, size: 15),
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: FilledButton.icon(
              onPressed: () {},
              label: const Text('狗狗', style: TextStyle(fontSize: 12)),
              icon: const Icon(Icons.pets, size: 15),
              // style: ButtonStyle(
              //   backgroundColor: MaterialStateProperty.all(Color(0xFFFFDAD9)),
              // ),
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: FilledButton.icon(
              onPressed: () {},
              label: const Text('龟龟', style: TextStyle(fontSize: 12)),
              icon: const Icon(Icons.pets, size: 15),
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: FilledButton.icon(
              onPressed: () {},
              label: const Text('其他', style: TextStyle(fontSize: 12)),
              icon: const Icon(Icons.pets, size: 15),
            ),
          ),
        ],
      ),
    );
  }
}

class InfiniteGridView extends StatefulWidget {
  const InfiniteGridView({super.key});

  @override
  _InfiniteGridViewState createState() => _InfiniteGridViewState();
}

class _InfiniteGridViewState extends State<InfiniteGridView> {
  List<IconData> _icons = []; //保存Icon数据

  @override
  void initState() {
    super.initState();
    // 初始化数据
    _retrieveIcons();
  }

  @override
  Widget build(BuildContext context) {
    return GridView.builder(
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2, //每行2列
        childAspectRatio: 0.5, //显示区域宽高比
        mainAxisSpacing: 10,
        crossAxisSpacing: 10,
      ),
      itemCount: _icons.length,
      itemBuilder: (context, index) {
        //如果显示到最后一个并且Icon总数小于200时继续获取数据
        if (index == _icons.length - 1 && _icons.length < 200) {
          _retrieveIcons();
        }
        return Container(
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(8),
            boxShadow: [
              BoxShadow(
                color: Colors.grey.withOpacity(0.5),
                spreadRadius: 2,
                blurRadius: 5,
                offset: Offset(0, 3),
              ),
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Expanded(
                child:
                    Image.asset('assets/images/image.png', fit: BoxFit.cover),
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  '我是标题我是标题我是标题我是标题我是标题',
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              Container(
                margin: EdgeInsets.only(bottom: 8),
                child: Row(
                  children: [
                    Expanded(
                      child: Padding(
                        padding: EdgeInsets.only(left: 8),
                        child: Row(
                          children: const [
                            CircleAvatar(
                              radius: 11,
                              backgroundImage:
                                  AssetImage('assets/images/image.png'),
                            ),
                            SizedBox(width: 8),
                            Text(
                              'cxyyyy',
                              style: TextStyle(
                                fontSize: 12,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                    Padding(
                      padding: EdgeInsets.only(right: 8),
                      child: Icon(
                        Icons.favorite_border,
                        color: Colors.red,
                        size: 15,
                      ),
                    ),
                  ],
                ),
              )
            ],
          ),
        );
      },
    );
  }

  //模拟异步获取数据
  void _retrieveIcons() {
    Future.delayed(Duration(milliseconds: 200)).then((e) {
      setState(() {
        _icons.addAll([
          Icons.ac_unit,
          Icons.airport_shuttle,
          Icons.all_inclusive,
          Icons.beach_access,
          Icons.cake,
          Icons.free_breakfast,
        ]);
      });
    });
  }
}
