import matplotlib.pyplot as plt

fig=plt.figure(figsize=(7,5))
name=["avinash","jacob","michealle","sally"]
scores=[89,78,93,57]
scores2=[95,85,87,78]
position=[0,1,2,3]
position2=[0.3,1.3,2.3,3.3]
position3=[0.15,1.15,2.15,3.15]
plt.bar(position,scores,width=0.3,color="g")
plt.bar(position2,scores2,width=0.3)
plt.title("Latest Test score")



plt.show()