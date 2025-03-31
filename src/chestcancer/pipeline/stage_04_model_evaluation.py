from chestcancer.config.configuration import ConfigurationManager
from chestcancer.components.model_evaluation import Evaluation
from chestcancer import logger
from chestcancer.mlflow_logger import init_dagshub
from chestcancer.constants import *

STAGE_NAME = "Evaluation Stage"



class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        init_dagshub(REPO_OWNER, REPO_NAME)
# Run Evaluation Pipeline

        config_manager = ConfigurationManager()
        eval_config = config_manager.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e