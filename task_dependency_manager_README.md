# Task Dependency Manager

## Problem Description
Implement a system to manage tasks with dependencies, ensuring tasks are executed in the correct order and detecting any circular dependencies that would make execution impossible.

## Features
1. Add tasks with or without dependencies
2. Detect circular dependencies
3. Generate valid execution order (topological sort)
4. Find prerequisites for any task
5. Find dependent tasks for any task

## Implementation Details

### Data Structures Used
1. **Adjacency List (Graph)**: Store task dependencies
2. **Reverse Graph**: Store task prerequisites
3. **Set**: Track all tasks
4. **Queue**: Used in BFS for cycle detection and topological sort

### Key Algorithms
1. **Cycle Detection**: 
   - Uses BFS to detect potential cycles when adding dependencies
   - Prevents creation of circular dependencies

2. **Topological Sort**:
   - Uses Kahn's algorithm
   - Tracks in-degree of each node
   - Returns None if cycle exists

3. **Dependency Traversal**:
   - Uses BFS to find all prerequisites/dependents
   - Handles both direct and indirect dependencies

### Time Complexity
- Add Task: O(1)
- Add Dependency: O(V + E) for cycle detection
- Get Execution Order: O(V + E)
- Get Prerequisites/Dependents: O(V + E)
Where V is number of tasks and E is number of dependencies

### Space Complexity
- O(V + E) for storing the graph and reverse graph

## Edge Cases Handled
- Circular dependencies
- Non-existent tasks
- Duplicate tasks/dependencies
- Multiple dependencies for same task
- Tasks with no dependencies/dependents

## Usage Example
```python
manager = TaskDependencyManager()
manager.add_dependency("Learn Django", "Learn Python")
manager.add_dependency("Learn Django", "Learn SQL")
manager.add_dependency("Build Web App", "Learn Django")

# Get execution order
order = manager.get_execution_order()
# Returns: ["Learn Python", "Learn SQL", "Learn Django", "Build Web App"]

# Get prerequisites for "Build Web App"
prereqs = manager.get_prerequisites("Build Web App")
# Returns: {"Learn Python", "Learn SQL", "Learn Django"}
```

## Applications
- Project Management
- Build Systems
- Workflow Automation
- Course Prerequisites
- Software Deployment
- Task Scheduling with Dependencies
