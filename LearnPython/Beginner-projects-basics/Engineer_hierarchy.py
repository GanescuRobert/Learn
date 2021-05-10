class Engineer:
	def __init__(self,license_no):
		self.license_no = license_no
	def designe_project(self):
		print(self.license_no,'\tI am designing a project.')

class SeniorEngineer(Engineer):
	def __init__(self,license_no,num_projects):
		super().__init__(license_no)
		self.num_projects = num_projects
	def deal_project(self):
		print(self.license_no,'\tI have a project to do.')
		self.num_projects += 1

class SeniorComputerEngineer(SeniorEngineer):
	def __init__(self,license_no,num_projects,current_project):
		super().__init__(license_no,num_projects)
		self.current_project = current_project

A = Engineer('A1234')
A.designe_project()

B = SeniorEngineer('B1234',10)
B.deal_project()
print('Number of projects made by B: ',B.num_projects)

C = SeniorComputerEngineer('C1234',100,'network connection')
print (C.current_project)
