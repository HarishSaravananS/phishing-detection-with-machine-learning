from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    test_path: Path
    train_path: Path
    

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    train_path: Path
    test_path:Path
    train_y_path:Path
    test_y_path:Path    



@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir:Path
    file_path:Path

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir:Path
    file_path:Path
    models_path:Path    