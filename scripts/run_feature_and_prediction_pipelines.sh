#!/bin/bash

set -e

cd pipeline

# Run the feature pipeline
jupyter nbconvert --to notebook --execute 2_feature_pipeline.ipynb

# Run the batch inference pipeline (xgboost)
jupyter nbconvert --to notebook --execute 4_1_inference_pipeline_xgb.ipynb

# Run the batch inference pipeline (lstm)
jupyter nbconvert --to notebook --execute 4_2_inference_pipeline_lstm.ipynb