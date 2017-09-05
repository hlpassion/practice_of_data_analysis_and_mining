## 总结
了解输出混淆矩阵方法

```
from sklearn import metrics
metrics.confusion_matrix(y_train, model.predict(x_train))
```

- 图像分类中图像处理方法常用直方图法或者颜色矩阵
- 图像特征提取可以使用，一阶颜色矩（反映图像整体明暗程度），二阶颜色矩（反映图像颜色分布范围），三阶颜色矩（反映颜色分布对称性）
- SVM模型中，可以适当采用放大特征的方式提高区分度和准确率

