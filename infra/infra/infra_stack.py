import aws_cdk

from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api_image_code = _lambda.DockerImageCode.from_image_asset(
            "../app",
            cmd=["api_handler.handler"],
            build_args={
                "platform": "linux/amd64",
            },
        )

        api_function = _lambda.DockerImageFunction(
            self,
            "model_serving_endpoint",
            architecture=_lambda.Architecture.X86_64,
            code=api_image_code,
            timeout=Duration.seconds(30),
            memory_size=128,
        )

        function_url = api_function.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE,
        )

        aws_cdk.CfnOutput(self, "FunctionUrl", value=function_url.url)