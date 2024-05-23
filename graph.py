import numpy as np
import matplotlib.pyplot as plt
objects=('cancer','heart disease','typhoid','jaundice','malaria','dengue')
y_pos=np.arange(len(objects))
performance=[3,2,2,1,1,1]
plt.barh(y_pos,performance,align='center',color='b')
plt.yticks(y_pos,objects)
plt.xlabel('number of patients')
plt.title('disease frequency chart')
plt.show()
