# from TextSummariser.src.textSummariser.pipeline.stage_1_data_ingestion import DataIngestionPipelineStage1
# from src.textSummariser.logging import logger
#
# STAGE_NAME="Data Ingestion Stage"
#
# try:
#     logger.info(f">>>>>>>>>>>{STAGE_NAME} started !<<<<<<<<<<<<<<<<<<<<<")
#     injestion_pipeline = DataIngestionPipelineStage1()
#     injestion_pipeline.main()
# except Exception as e:
#     logger.error(e)
#     raise e
#
#
class Parent:
    def show(self):
        print ("Parent's show method")


class A (Parent):
    def show(self):
        print ("A's show method")


class B (A):
    def show(self):
        print ("B's show method")


class X (Parent):
    def show(self):
        print ("X's show method")


class Y (X):
    def show(self):
        print ("Y's show method")


class C (Y, B):
    def show(self):
        print ("C's show method")


c = C ()
c.show ()
print (C.mro ())

A.__init_subclass__ (B)
