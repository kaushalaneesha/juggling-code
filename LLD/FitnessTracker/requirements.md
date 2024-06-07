A fitness tracking application that provides insights and information on your fitness
- Histoy
- Fitness goals
- Daily progress
    - steps
- Actionable insights

- Number of steps in a day
- calories in a day
- number of minutes worked out
- average heartbeat
- water intake

Goals : get rewards 
- rewards if done the goal
- motivation 
 - if reached 80% of the goal
 - far away from the 
 

SystemConfig
    - motivation_percent 
    - pickup_percent

 Entities 
 - Goal 
    - WaterGoal
    - StepGaol
    - CaloryGoal
    - MinWorkoutGoal 

Analytics
goal_history <user_id, date, goal>

Profile
 - id
 - hearbeat
 - goals: List[Goal]


Goal
 - goal_type: str
 - curr_value: int
 - expected_value: int



GoalManager
- nearGoal(user, goal)
- farGoal(user, goal)

- resetGoal()

