class Matrix:


    def __init__(self, m_list):
        self.m_list = m_list

    @property
    def m_list(self):
        return self.__m_list

    @m_list.setter
    def m_list(self, asd):
        if len(max(asd, key = len)) != len(min(asd, key = len)):
            print('Матрица заполенна не до конца,\
для дальнейшей работы произведено заполнение "0"')
            for i in range(len(asd)):
                while len(asd[i]) < len(max(asd, key = len)):
                    asd[i].append(0)
            self.__m_list = asd
        else:
            self.__m_list = asd
                    
    def __str__(self):
        #Размер ячейки матрици
        
        cell_weight = len(str(max(map(max, self.m_list)))) + 1
        return ''.join(''.join(str(j).rjust(cell_weight)
                for j in i) + '\n'
                for i in self.m_list)

    def __add__(self, other):
        if (len(self.m_list) == len(other.m_list) and
            len(self.m_list[0]) == len(other.m_list[0])):
            for i in range(len(self.m_list)):
                for j in range(len(range(len(self.m_list[0])))):
                    self.m_list[i][j] += other.m_list[i][j]
            return Matrix(self.m_list)
        else: return 'Разные размерности матриц'



m_1 = Matrix([[1,2,9],[3,4],[5,6]])
m_2 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(m_1 + m_2)
