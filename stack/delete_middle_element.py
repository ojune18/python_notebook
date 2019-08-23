from stack import Stack

class DeleteMid(Stack):

    def delete_mid(self,i=None,stop=None):

        if i is None:
            i = self.size()
            stop=self.size()

        if i is not None and not self.isEmpty():
            if i > stop//2:
                c = self.pop()
                self.delete_mid(i-1,stop)
                self.push(c)
            if i == stop//2:
                self.pop()


        return self._item



d = DeleteMid()

d.push(5)
d.push(10)
d.push(3)
d.push(2)
d.push(22)

print(d.delete_mid())