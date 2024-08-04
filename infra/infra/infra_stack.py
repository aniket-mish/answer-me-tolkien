from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_endpoint = _lambda.DockerImageFunction(
            self,
            "model_serving_endpoint",
            function_name="inf_func",
            architecture=_lambda.Architecture.X86_64,
            code=_lambda.DockerImageCode.from_image_asset(
                "../rag_app_image",
                cmd=["api_handler.handler"],
                build_args={
                    "platform": "linux/amd64",
                },
            ),
            timeout=Duration.seconds(60),
            memory_size=128,
        )

        function_url = lambda_endpoint.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE,
        )