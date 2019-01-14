import logging
import logging.config


LOGGING = {
   'version': 1,
   'disable_existing_loggers': True,
   'formatters': {
       'verbose': {
           'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
       },
       'simple': {
           'format': '%(levelname)s %(message)s'
       },
   },
   'handlers': {
       'null': {
           'level': 'DEBUG',
           'class': 'logging.NullHandler',
       },
       'console': {
           'level': 'DEBUG',
           'class': 'logging.StreamHandler',
           'formatter': 'verbose'
       },
       'file': {
           'level': 'INFO',
           'class': 'logging.FileHandler',
           'filename': 'fight_logs.txt',
           'mode': 'w',
           'formatter': 'verbose'
       },
       'consoleError': {
           'level': 'ERROR',
           'class': 'logging.StreamHandler',
           'formatter': 'simple'
       }
   },
   'loggers': {
       'null': {
           'handlers': ['null'],
           'propagate': True,
           'level': 'INFO',
       },
       'Fight_log': {
           'handlers': ['file'],
           'level': 'DEBUG',
           'propagate': True,
       },
       'Create': {
           'handlers': ['console'],
           'level': 'INFO'
       }
   }
}


def create_logs(all_armies):
    logging.config.dictConfig(LOGGING)
    log_fight = logging.getLogger('Fight_log')
    log_create = logging.getLogger('Create')
    log_info = logging.getLogger("Create")

    log_info.info("Create armies")
    for army in all_armies:
        log_create.info("%s has %s squads", army, len(army.squads))
        for squad in army.squads:
            log_create.info("   Squad: %s has %s units", squad, len(squad.members))
            for member in squad.members:
                log_create.info("       Member: %s", member.name)

    log_info.info("End create")
    log_info.info("START FIGHT")
    return log_fight, log_info
