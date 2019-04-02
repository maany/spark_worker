import argparse
import yaml
import yaql

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--site_config', help="Compiled Site Level Configuration YAML file")
    parser.add_argument('--execution_id', help="ID of lightweight component")
    parser.add_argument('--output_dir', help="Output directory")
    args = parser.parse_args()
    return {
        'augmented_site_level_config_file': args.site_config,
        'execution_id': args.execution_id,
        'output_dir': args.output_dir
    }


def get_current_lightweight_component(data, execution_id):
    current_lightweight_component = None
    for lightweight_component in data['lightweight_components']:
        if lightweight_component['execution_id'] == int(execution_id):
            current_lightweight_component = lightweight_component
            break
    return current_lightweight_component


def get_spark_default_config_file_content(data, execution_id):
    current_lightweight_component = get_current_lightweight_component(data, execution_id)
    config = []
    config_section = current_lightweight_component['config']
    spark_eventLog_enabled = config_section['spark_eventLog_enabled']
    config.append("spark.eventLog.enabled {value}".format(value=str(spark_eventLog_enabled).lower()))
    spark_ui_enabled = config_section['spark_ui_enabled']
    config.append("spark.ui.enabled {value}".format(value=str(spark_ui_enabled).lower()))
    # process supplemental config
    supplemental_config = current_lightweight_component['supplemental_config']
    for config_file in supplemental_config:
            if config_file == "spark-defaults.conf":
                for config_value in supplemental_config['spark-defaults.conf']:
                    config.append(config_value)
    return "\n".join(config)


if __name__ == "__main__":
    args = parse_args()
    execution_id = args['execution_id']
    site_config_filename =  args['augmented_site_level_config_file']
    site_config = open(site_config_filename, 'r')
    data = yaml.load(site_config)
    output_dir = args['output_dir']
    spark_default_config_file = open("{output_dir}/spark-defaults.conf".format(output_dir=output_dir), 'w')
    spark_default_config_file.write(get_spark_default_config_file_content(data, execution_id))
    spark_default_config_file.close()













