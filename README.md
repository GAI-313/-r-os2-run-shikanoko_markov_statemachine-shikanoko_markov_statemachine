# shikanoko_markov_statemachine
<center>
<video src="https://github.com/user-attachments/assets/29a518b3-5236-4c01-91fd-1070f41b2cdd" controls="true" >
</center>
  
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
