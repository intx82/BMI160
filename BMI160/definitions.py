from micropython import const

## bit field offsets and lengths
ACC_PMU_STATUS_BIT  = const(4)
ACC_PMU_STATUS_LEN  = const(2)
GYR_PMU_STATUS_BIT  = const(2)
GYR_PMU_STATUS_LEN  = const(2)
GYRO_RANGE_SEL_BIT  = const(0)
GYRO_RANGE_SEL_LEN  = const(3)
GYRO_RATE_SEL_BIT   = const(0)
GYRO_RATE_SEL_LEN   = const(4)
GYRO_DLPF_SEL_BIT   = const(4)
GYRO_DLPF_SEL_LEN   = const(2)
ACCEL_DLPF_SEL_BIT  = const(4)
ACCEL_DLPF_SEL_LEN  = const(3)
ACCEL_RANGE_SEL_BIT = const(0)
ACCEL_RANGE_SEL_LEN = const(4)

## Gyroscope Sensitivity Range options
# see setFullScaleGyroRange()
GYRO_RANGE_2000     = const(0)    # +/- 2000 degrees/second
GYRO_RANGE_1000     = const(1)    # +/- 1000 degrees/second
GYRO_RANGE_500      = const(2)    # +/-  500 degrees/second
GYRO_RANGE_250      = const(3)    # +/-  250 degrees/second
GYRO_RANGE_125      = const(4)    # +/-  125 degrees/second

## Accelerometer Sensitivity Range options
# see setFullScaleAccelRange()
ACCEL_RANGE_2G      = const(0X03) # +/-  2g range
ACCEL_RANGE_4G      = const(0X05) # +/-  4g range
ACCEL_RANGE_8G      = const(0X08) # +/-  8g range
ACCEL_RANGE_16G     = const(0X0C) # +/- 16g range

FOC_ACC_Z_BIT       = const(0)
FOC_ACC_Z_LEN       = const(2)
FOC_ACC_Y_BIT       = const(2)
FOC_ACC_Y_LEN       = const(2)
FOC_ACC_X_BIT       = const(4)
FOC_ACC_X_LEN       = const(2)
FOC_GYR_EN          = const(6)

ACCEL_RATE_SEL_BIT   = const(0)
ACCEL_RATE_SEL_LEN   = const(4)

# GYRO_RATE_6_25HZ      = const(0x04)
# GYRO_RATE_12_5HZ      = const(0x05)
GYRO_RATE_25HZ      = const(0x06)
GYRO_RATE_50HZ      = const(0x07)
GYRO_RATE_100HZ      = const(0x08)
GYRO_RATE_200HZ      = const(0x09)
GYRO_RATE_400HZ      = const(0x0A)
GYRO_RATE_800HZ      = const(0x0B)
GYRO_RATE_1600HZ      = const(0x0C)
GYRO_RATE_3200HZ      = const(0x0D)

ACCEL_RATE_0_78HZ      = const(0x01)
ACCEL_RATE_1_56HZ      = const(0x02)
ACCEL_RATE_3_12HZ      = const(0x03)
ACCEL_RATE_6_25HZ      = const(0x04)
ACCEL_RATE_12_5HZ      = const(0x05)
ACCEL_RATE_25HZ      = const(0x06)
ACCEL_RATE_50HZ      = const(0x07)
ACCEL_RATE_100HZ      = const(0x08)
ACCEL_RATE_200HZ      = const(0x09)
ACCEL_RATE_400HZ      = const(0x0A)
ACCEL_RATE_800HZ      = const(0x0B)
ACCEL_RATE_1600HZ      = const(0x0C)

ACC_OFFSET_EN = const(6)