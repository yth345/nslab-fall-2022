## 0930 Location Set Cover

- Task: Find the min location set that can cover all edge server IPs
- Data duration: April to July, 2021
- Involved countries: 18 (Australia, Brazil, Canada, Denmark, France, Germany, Italy, 
Japan, Netherlands, Poland, Russia, South Korea, Spain, Sweden, Turkey, Ukraine, United Kingdom, United States)

### 1. Greedy Algorithm

- Idea: For each round, select the country that can find the most undiscovered servers
- Result: 12 countries
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

- Idea: Use brute force method to try all combinations of countries, C(18, 1), C(18, 2), ..., C(18, 18). Since a set cover is found using 12 countries by greedy algorithm, I try combinations starting from C(18, 10).
- Result: 12 countries, same as the result using greedy algorithm.
  ```
  C(18, 10) set cover not found
  C(18, 11) set cover not found
  C(18, 12) found, combination: ['Brazil', 'South_Korea', 'United_Kingdom', 'Canada', 'France', 'Netherlands', 'Germany', 'Japan', 'Australia', 'Sweden', 'Italy', 'United_States']
  ```
  
### 3. Summary
- We can get the minimum set cover using greedy algorithm in this case.
- Countries contributed (12): Australia, Brazil, Canada, France, Germany, Italy, Japan, Netherlands, South Korea, Sweden, UK, US
- Countries unused (6): Denmark, Poland, Russia, Spain, Turkey, Ukraine
