import logging
import sys
from pathlib import Path



sys.path.append('../src/')

import confighandler as cfg
from confighandler.controller.custom_types.SelectableList import SelectableList
from LaserConfig import LaserConfig


class ApplicationConfig(cfg.ConfigNode):

    def __init__(self, internal_log=True, internal_log_level= logging.DEBUG) -> None:
        super().__init__(internal_log=internal_log, internal_log_level=internal_log_level)

        self.output_directory: cfg.Field[Path] = cfg.Field(Path("C:\\{wafer_nr}"))

        self.wafer_version: cfg.Field[str] = cfg.Field("v1.0",
                                                       friendly_name="wafer_version",
                                                       description="The version of the wafer")

        self.wafer_number: cfg.Field[int] = cfg.Field(1,
                                                      friendly_name="wafer_number",
                                                      description="The version of the wafer")

        self.check: cfg.Field[bool] = cfg.Field(False, friendly_name="testcheck",
                                                      description="Testcheck")


        self.wafer_nr: cfg.Field[str] = cfg.Field("12345ABCD_{wafer_number}",
                                                  friendly_name="wafer_nr",
                                                  description="The version of the wafer")

        self.wafer_number2: cfg.Field[tuple] = cfg.Field((1, 2),
                                                         friendly_name="wafer_number2",
                                                         description="The version of the wafer")

        self.wafer_list: cfg.Field[list] = cfg.Field([1, 2],
                                                     friendly_name="wafer_list",
                                                     description="The version of the wafer")

        self.wafer_list1: cfg.Field[list] = cfg.Field(SelectableList(
            ['a', 'b', 'c'], selected_index=0),
                                                     friendly_name="wafer_list1",
                                                     description="The version of the wafer")

        self.laser_config: LaserConfig = LaserConfig(internal_log=internal_log,
                                                     internal_log_level=internal_log_level)


        self.register()
