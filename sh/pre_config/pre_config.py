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

if __name__ == "__main__":
    args = parse_args()
    id = args['execution_id']
    site_config_filename =  args['augmented_site_level_config_file']
    site_config = open(site_config_filename, 'r')
    data = yaml.load(site_config)
    output_dir = args['output_dir']