# shikanoko_markov_statemachine
<image src="https://i.imgur.com/I6bvHIH.mp4">

　「しかのこのこのここしたんたん」のマルコフ連鎖を StateMachine として動作させるパッケージ

## インストール
```
rosdep update; rosdep install -i --from-path src
colcon build --packages-select shikanoko_markov_statemachine
```

## 実行
```
ros2 run shikanoko_markov_statemachine shikanoko_markov_statemachine
```
