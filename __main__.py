import pulumi
import pulumi_random as random

random_number = random.Integer("randomNumber", min=1, max=100)

# Export the random number result
pulumi.export("random_number", random_number.result)
