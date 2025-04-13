"""
Problem: Task Dependency Manager

Implement a system to manage tasks with dependencies. The system should:
1. Add tasks and their dependencies
2. Detect circular dependencies
3. Get tasks in order of execution (topological sort)
4. Find all prerequisites for a given task
5. Find all dependent tasks for a given task

Example:
- Task "Learn Python" must be completed before "Learn Django"
- Task "Learn SQL" must be completed before "Learn Django"
- Task "Learn Django" must be completed before "Build Web App"

The system should return tasks in valid execution order and detect any circular dependencies.
"""

from collections import defaultdict, deque
from typing import List, Set, Dict, Optional, Tuple

class TaskDependencyManager:
    def __init__(self):
        # Adjacency list for dependencies (task -> tasks that depend on it)
        self.graph: Dict[str, Set[str]] = defaultdict(set)
        # Reverse graph for prerequisites (task -> tasks it depends on)
        self.prerequisites: Dict[str, Set[str]] = defaultdict(set)
        # Set of all tasks
        self.tasks: Set[str] = set()
    
    def add_task(self, task: str) -> bool:
        """Add a task without any dependencies."""
        if task in self.tasks:
            return False
        self.tasks.add(task)
        return True
    
    def add_dependency(self, task: str, depends_on: str) -> bool:
        """Add a dependency: task depends on depends_on."""
        # Add tasks if they don't exist
        self.tasks.add(task)
        self.tasks.add(depends_on)
        
        # Check if this would create a cycle
        if self._would_create_cycle(task, depends_on):
            return False
        
        # Add dependency
        self.graph[depends_on].add(task)
        self.prerequisites[task].add(depends_on)
        return True
    
    def _would_create_cycle(self, task: str, depends_on: str) -> bool:
        """Check if adding this dependency would create a cycle."""
        if task == depends_on:
            return True
        
        # Do BFS from depends_on, if we can reach task, there's a cycle
        visited = set()
        queue = deque([depends_on])
        
        while queue:
            current = queue.popleft()
            if current == task:
                return True
            
            if current in visited:
                continue
                
            visited.add(current)
            queue.extend(self.graph[current])
        
        return False
    
    def get_execution_order(self) -> Optional[List[str]]:
        """Return tasks in topological order (None if cycle exists)."""
        # Calculate in-degree for each task
        in_degree = defaultdict(int)
        for task in self.tasks:
            for dependent in self.graph[task]:
                in_degree[dependent] += 1
        
        # Start with tasks that have no dependencies
        queue = deque([task for task in self.tasks if in_degree[task] == 0])
        result = []
        
        while queue:
            task = queue.popleft()
            result.append(task)
            
            # Reduce in-degree of dependent tasks
            for dependent in self.graph[task]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
        
        # If we couldn't process all tasks, there must be a cycle
        return result if len(result) == len(self.tasks) else None
    
    def get_prerequisites(self, task: str) -> Set[str]:
        """Get all tasks that must be completed before this task."""
        if task not in self.tasks:
            return set()
        
        result = set()
        queue = deque([task])
        
        while queue:
            current = queue.popleft()
            for prereq in self.prerequisites[current]:
                if prereq not in result:
                    result.add(prereq)
                    queue.append(prereq)
        
        return result
    
    def get_dependents(self, task: str) -> Set[str]:
        """Get all tasks that depend on this task."""
        if task not in self.tasks:
            return set()
        
        result = set()
        queue = deque([task])
        
        while queue:
            current = queue.popleft()
            for dependent in self.graph[current]:
                if dependent not in result:
                    result.add(dependent)
                    queue.append(dependent)
        
        return result

def test_task_dependency_manager():
    manager = TaskDependencyManager()
    
    print("Test 1: Adding Tasks and Dependencies")
    print("Adding Learn Python:", manager.add_task("Learn Python"))
    print("Adding Learn SQL:", manager.add_task("Learn SQL"))
    print("Adding Learn Django (depends on Python):", 
          manager.add_dependency("Learn Django", "Learn Python"))
    print("Adding Learn Django (depends on SQL):", 
          manager.add_dependency("Learn Django", "Learn SQL"))
    print("Adding Build Web App (depends on Django):", 
          manager.add_dependency("Build Web App", "Learn Django"))
    print("-" * 50)
    
    print("\nTest 2: Detecting Circular Dependencies")
    print("Adding circular dependency (Web App -> Python):", 
          manager.add_dependency("Learn Python", "Build Web App"))
    print("-" * 50)
    
    print("\nTest 3: Getting Execution Order")
    order = manager.get_execution_order()
    if order:
        print("Valid execution order:", " -> ".join(order))
    else:
        print("No valid execution order (cycle detected)")
    print("-" * 50)
    
    print("\nTest 4: Prerequisites for 'Build Web App'")
    prereqs = manager.get_prerequisites("Build Web App")
    print("Prerequisites:", prereqs)
    print("-" * 50)
    
    print("\nTest 5: Dependents of 'Learn Python'")
    deps = manager.get_dependents("Learn Python")
    print("Dependents:", deps)
    print("-" * 50)
    
    # Test with a new manager to show valid execution order
    print("\nTest 6: Valid Execution Order (New Manager)")
    manager2 = TaskDependencyManager()
    manager2.add_dependency("Learn Django", "Learn Python")
    manager2.add_dependency("Learn Django", "Learn SQL")
    manager2.add_dependency("Build Web App", "Learn Django")
    
    order = manager2.get_execution_order()
    if order:
        print("Valid execution order:", " -> ".join(order))
    else:
        print("No valid execution order (cycle detected)")

if __name__ == "__main__":
    test_task_dependency_manager()
