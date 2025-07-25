#CDK Code
from aws_cdk import ( 
    aws_iam as iam,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_ecr_assets as ecr_assets,
    Stack
)
from constructs import Construct
from aws_cdk.aws_ec2 import Vpc

class LinkedListApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = Vpc(self, "LinkedListVpc", max_azs=2)

        cluster = ecs.Cluster(self, "LinkedListCluster", vpc=vpc)

        image = ecr_assets.DockerImageAsset(self, "LinkedListImage", 
            directory=".",
            build_args={
                "PYTHON_VERSION": "3.11-slim"
            }
        )

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "LinkedListService",
            cluster = cluster,
            cpu = 256,
            desired_count = 1,
            memory_limit_mib = 1024,
            task_image_options = ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_docker_image_asset(image),
                container_port = 80
            ),
            public_load_balancer=True,
            runtime_platform=ecs.RuntimePlatform(
                cpu_architecture=ecs.CpuArchitecture.ARM64,
                operating_system_family=ecs.OperatingSystemFamily.LINUX
            )
        )
