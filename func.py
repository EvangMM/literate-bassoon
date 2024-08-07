from digitalhub_runtime_python import handler
import pandas as pd

def init(context):
    context.logger.info("===========================================================================================")


@handler(outputs=["data", "test"])
def downloader(di, col: str, project):#, context, event):

    data = {col: [1,2,3]}
    df = di.as_df(
    )

    xxx="aaa.json"
    with open(xxx, "w") as f:
        f.write("{}")
        
    project.log_artifact(name="kjljlk", kind="artifact", source=xxx)
    project.log_model(name="kjljlk", kind="model", source=xxx)
    project.log_dataitem(name="kjljlk", kind="table", data=df)
    return df, "label"
