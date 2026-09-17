Using the [mdsplus_first_acess.ipynb](src/mdsplus_first_acess.ipynb) function in the `src` directory, we can access the TCABR MDSplus server. For this example, we used shot 33668 and accessed the Mirnov, SXR, and $H_\alpha$ diagnostics. From these data, we identified the following available channels:

- Mirnov diagnostics: channels from 01 to 24, with nomeclature `BBMRNVN##.signal`.

- SXR diagnostics: channels from  01 to 20, with nomeclature `SOFTXR0##.signal`.

- $H_\alpha$ diagnostics: one channel, named `HALFAREF0.signal`.

For the channels investigated, each signal contains 100,000 points over a total time interval of approximately 200 ms. The stored signals are given in voltage units (V). The time step is approximately 1.9989 ms, corresponding to a sampling frequency of approximately 500.3 Hz.
