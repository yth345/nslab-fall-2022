## 0930 Server Set Cover

- Data collected from April to July, 2021
- Involved 18 countries (Australia, Brazil, Canada, Denmark, France, Germany, Italy, 
Japan, Netherlands, Poland, Russia, South_Korea, Spain, Sweden, Turkey, Ukraine, United_Kingdom, United_States)

### 1. Greedy Algorithm

- Idea: for each round, select the country that can find the most undiscovered servers
- Result:
  ```
  inital server count: 2689
  select United_Kingdom, undiscovered server count: 1205
  select United_States, undiscovered server count: 621
  select South_Korea, undiscovered server count: 365
  select Germany, undiscovered server count: 250
  select Brazil, undiscovered server count: 136
  select Australia, undiscovered server count: 89
  select Japan, undiscovered server count: 56
  select Canada, undiscovered server count: 25
  select France, undiscovered server count: 12
  select Netherlands, undiscovered server count: 4
  select Italy, undiscovered server count: 1
  select Sweden, undiscovered server count: 0
  
  selected countries:
  ['United_Kingdom', 'United_States', 'South_Korea', 'Germany', 'Brazil', 'Australia', 'Japan', 'Canada', 'France', 'Netherlands', 'Italy', 'Sweden']
  ```  

### 2. Brute Force Ground Truth

- Idea: use brute force method to find the actual min set cover
- Result:
