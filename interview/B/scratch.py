from django.db import models
from django.contrib.postgres.fields import ArrayField
import time
import thread
import pytemp

class Property(models.Model):
    name = models.CharField(max_length=200)

    def sync_pin_codes(self):
        # how does on ensure that the pincodes are the same for each lock on a property?
        pass

class Device(models.Model):
    on = models.BooleanField(default=False)
    serial_number = models.CharField()
    property_id = models.ForeignKey("Property", on_delete=models.CASCADE)


class Alarm(Device):
    volume = models.IntegerField(max=10, min=1, default=5)

    def silence(self, seconds=None):
        # send call to device to turn volume to 0 or silence or turn off alarm depending on iot function
        if seconds:
            thread.start_new_thread(self._temp_silence, seconds)

    def _temp_silence(self, seconds):
        time.sleep(seconds)
        # send call to device to turn volume to self.volume



class TemperatureSensor(Device):
    celsius = models.BooleanField(default=False)

    def get_temperature(self):
        temperature = self._GetTempFromIotDevice()
        if not self.celsius:
            temperature = pytemp(temperature,'celsius', 'fahrenheit')
        return temperature

    def _get_temp_from_iot_device(self):
        # send call to device and return its temp in celsius
        pass


class HumiditySensor(Device):
    target_humidity = models.IntegerField(default=10)

    def save(self):
        # call iot device to set target humidity. data:self.target_humidity
        return super(self).save()

    def get_current_humidity(self):
        humidity =  # call iot device to get humidity lvl. data: self.serial_number
        return humidity


class FloodSensor(Device):

    def get_flood_status(self):
        status =  # call iot device to get flood status.  data: self.serial_number
        return status


class SmokeSensor(Device):

    def get_smoke_levels(self):
        levels = #call iot device to get smoke levels.  data: self.serial_number
        return levels


class CarbonMonoxideSensor(Device):

    def get_co_levels(self):
        levels =  # call iot device to get CO levels.  data: self.serial_number
        return levels


class WindowSensor(Device):

    def get_current_status(self):
        status =  # call iot device to get window status.  data: self.serial_number
        # secured/unsecured
        return status


class Thermostat(TemperatureSensor):
    AC = "AC"
    HEATER = "HE"
    OFF = "NA"
    SETTINGS = [
        (AC, "AirConditioning"),
        (HEATER, "Heater"),
        (OFF, "Off")
    ]

    upper_temp_limit = models.IntegerField(defualt=85)
    lower_temp_limit = models.IntegerField(defualt=60)
    ac_heat_enabled = models.CharField(
        max_length=2,
        choices=SETTINGS,
        default=OFF,
    )

    def toggle_fan(self):
        self.on = not self.on
        # call device to turn fan on or off depending on state. data: self.serial_number, self.on
        self.save()

    def temporarily_turn_on_fan(self):  # for 5 minutes
        if not self.on:
            # call device and turn fan on. data: self.serial_number, True
            thread.start_new_thread(self._TempSilence, self)
        else:
            # unsure what could be the best recourse. maybe raise an exception about the fan already being on.
            # for now, do nothing
            pass


    def _fan_temp_on(self):
        five_minutes = 5*60
        time.sleep(five_minutes)
        # send call to device to turn fan off. data self.serial_number, False


class HumidityController(Thermostat):
    humidity_sensor = models.ForeignKey('HumiditySensor', on_delete=models.CASCADE)


class DoorLock(Device):
    pin_code_limit = models.IntegerField(default=None)
    pin_codes = ArrayField(models.CharField(max_length=8))
    auto_lock_timeout = models.IntegerField(default=None)

    def save(self):
        # Override Save to validate limit of pincodes
        if len(self.pin_codes) > self.pin_code_limit:
            raise ValidationError
        return super(self).save()

    def lock(self):
        # call device to lock it

    def unlock(self):
        # call device to lock it

    def add_pin_code(self, code):
        if not code or code == "":
            # log code not being passed, or raise error
            return
        code_length = len(code)
        if code_length not in [4, 6, 8]:
            # log code not formated properly, or raise error
            return
        self.pin_codes = self.pin_codes.push()
        # self.save() # maybe save here. not sure

    def remove_pin_code(self, code):
        if not code or code == "":
            # log code not being passed, or raise error
            return
        if code in self.pin_codes:
            self.pin_codes.pop(code)

    def factory_reset_codes(self):
        self.pin_codes = ["0000"]
        self.save()

    def get_lock_status(self):
        status = # call device to get status. data: self.serial_number
        return status


class AllInOneSensor(models.Model):
    humidity_sensor = models.ForeignKey('HumiditySensor', on_delete=models.SET_NULL)
    temp_sensor = models.ForeignKey('TemperatureSensor', on_delete=models.SET_NULL)
    alarm = models.ForeignKey('Alarm', on_delete=models.SET_NULL)
    flood_sensor = models.ForeignKey('FloodSensor', on_delete=models.SET_NULL)

    def save(self):
        # validate that all the sensors are part of the same property
        #   raise ValidationError
        return super(self).save()


class CombinationCOSmokeSensor(models.Model):
    alarm = models.ForeignKey('Alarm', on_delete=models.SET_NULL)
    smoke_detector = models.ForeignKey("SmokeSensor", on_delete=models.SET_NULL)
    carbon_monoxide_sensor = models.ForeignKey("CarbonMonoxideSensor", on_delete=models.SET_NULL)

    def save(self):
        # validate that all the sensors are part of the same property
        #   raise ValidationError
        return super(self).save()


## These functions could probably be apart of the Property Model

def IsSecured(property_id):
    """
    Is the property secured?
    :return: bool
    """
    # property = getproperty(property_id) # getproperty is in controller file
    # check for locks and window sensors
    # if property has locks:
    #   for lock in property_locks:
    #       if lock.get_lock_status != "secured":
    #           return False
    # if property has window sensors:
    #   for sensor in property_sensors:
    #       if sensor.get_current_status != "secured":
    #           return False
    return True


def GetPropertyTemp(property_id):
    """
    What is the temperature in the property
    :return: int
    """
    # considerations: are there multiple temp sensors for the property? which one takes priority
    pass


def GetHumidityLevel(property_id):
    """
    What is the humidity level in the property
    :return: int
    """
    # considerations: are there multiple humidity sensors for the property? which one takes priority
    pass


def SliencePropertyAlarms(property_id, seconds=None):
    """
    Silence all alarms on the property
    """
    # if this were a view, should this permanently silence the alarms or temporarily.
    # should probably have a view for each case.
    # raise error is unable to silence all the alarms
    pass


def SecureProperty(property_id):
    """
    Secure the whole property
    """
    # raise error if unable to secure property
    pass


def GetRemainingNumOfPinCodes(property_id):
    """
     How many more pin codes can the property hold?
    :return: int
    """
    # consideration: what if there isn't a pin code limit set for a lock? maybe return -1 for infinite or unknown
    pass
