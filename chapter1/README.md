
# Decay Involving Two Types of Nuclei

##摘要  
以Chapter one 中的习题1.4为任务，给出了包含两类核子的简单级联衰变模型，探究了不同ratio=![tauA](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/tauA.png)/![tauB](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/tauB.png)下的结果。

##背景介绍  
这里我们考虑简单的级联衰变：  
![formula3](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/formula3.png)  
我们知道，A的衰变服从指数规律，而B一方面不断衰变成C，另一当面却又不断从A处获得补充。该简单模型的微分表示为：  
![formula1](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/formula1.png)  
解析解为：  
![formula4](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/formula4.png)  
![formula5](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/formula5.png)  
其中，这里假定开始时，B的数量为0。  
当![formula6](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/formula6.png)，即子核寿命远小于母核寿命时，子核B将按照母核A的规律衰变。  

##正文  

###实现原理  

####常微分方程组的数值近似解   
级联衰变模型对应的常微分方程可写成   
![formula2](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/formula2.png)  
若取dt为某一足够小的近似值，当已知N的初值N(t<sub>0</sub>)后多次迭代，便可得到之后所有的数值近似解。  

####参数设置  
- 这里简单得假设B的初始数量为0，![tauB](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/tauB.png)=1，ratio=![tauA](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/tauA.png)/![tauB](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/tauB.png)
- 对于此方程，需要设置的参数有ratio，![tauA](https://github.com/SmallGuoguo/computationalphysics_N2013301020033/blob/master/chapter1/resources/tauA.png)，N<sub>A</sub> (t<sub>0</sub>)，dt，time。  
  

####作图工具  
本次作业使用作图工具为matplotlib库。

###程序实现  

python源码地址：

###结果分析  



##结论  



##致谢  
使用了[whuCanon](https://github.com/whuCanon/computationalphysics_N2013301020085/blob/master/chapter1/README.md)的写作模板，感谢！
