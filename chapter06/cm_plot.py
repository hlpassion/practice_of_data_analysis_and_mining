def cm_plot(y, yp):
  
  from sklearn.metrics import confusion_matrix #µ¼Èë»ìÏý¾ØÕóº¯Êý

  cm = confusion_matrix(y, yp) #»ìÏý¾ØÕó
  
  import matplotlib.pyplot as plt #µ¼Èë×÷Í¼¿â
  plt.matshow(cm, cmap=plt.cm.Greens) #»­»ìÏý¾ØÕóÍ¼£¬ÅäÉ«·ç¸ñÊ¹ÓÃcm.Greens£¬¸ü¶à·ç¸ñÇë²Î¿¼¹ÙÍø¡£
  plt.colorbar() #ÑÕÉ«±êÇ©
  
  for x in range(len(cm)): #Êý¾Ý±êÇ©
    for y in range(len(cm)):
      plt.annotate(cm[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
  
  plt.ylabel('True label') #×ø±êÖá±êÇ©
  plt.xlabel('Predicted label') #×ø±êÖá±êÇ©
  return plt