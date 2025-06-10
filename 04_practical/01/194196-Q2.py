stack = []

print(type(stack))

print(f"Initial stack: {stack}")

stack.append(20)
stack.append(40)
stack.append(50)
stack.append(60)
stack.append(70)
stack.append(80)

print(f"After pushing: {stack}")

popped_item = stack.pop()
print(f"Popped item: {popped_item}")
print(f"Stack after pop: {stack}")

if stack:
    print(f"Top of stack(peek): {stack[-1]}")
else:
    print("Stack is empty")

print(f"Is stack empty? {len(stack) == 0}")
