# shikanoko_markov_statemachine
```
<div><video controls src="shikanoko_markov_statemachine.mp4" muted="false"></video></div>
```

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
