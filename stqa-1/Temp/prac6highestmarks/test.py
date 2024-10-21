from selenium import webdriver
from selenium.webdriver.common.by import By
def test():
    sub1highestmarks = {"student":"","marks":0,"sub":"sub-1"}
    sub2highestmarks = {"student":"","marks":0,"sub":"sub-2"}
    sub3highestmarks = {"student":"","marks":0,"sub":"sub-1"}
    driver = webdriver.Edge()
    driver.get("http://127.0.0.1:3000")
    table =driver.find_element(By.ID,"mytab")
    rows = table.find_elements(By.TAG_NAME,"tr")
    students_with_60_marks=[]
    
    for row in rows[1:]:
        
        cell = row.find_elements(By.TAG_NAME,"td")
        if(
            int(cell[3].text) >=60 or
            int(cell[4].text) >=60 or
            int(cell[5].text) >=60):
            students_with_60_marks.append([
                cell[1].text,
                cell[2].text,
                int(cell[3].text),
                int(cell[4].text),
                int(cell[5].text),])
    for student in students_with_60_marks:
        if student[2] > sub1highestmarks["marks"]:
            sub1highestmarks["student"] = student[0]
            sub1highestmarks["marks"] = student[2]
            
        if student[3] > sub2highestmarks["marks"]:
            sub2highestmarks["student"] = student[0]
            sub2highestmarks["marks"] = student[3]
        if student[4] > sub3highestmarks["marks"]:
            sub3highestmarks["student"] = student[0]
            sub3highestmarks["marks"] = student[4]
    print(sub1highestmarks)
    print(sub2highestmarks)
    print(sub3highestmarks)
    driver.quit()
test()
            
      