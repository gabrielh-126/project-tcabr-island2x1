Using the [mdsplus_first_acess.ipynb](../src/mdsplus_first_acess.ipynb) function in the `src` directory, we can access the TCABR MDSplus server. For this example, we used shot 33668 and accessed the Mirnov, SXR, and $H_\alpha$ diagnostics. From these data, we identified the following available channels:

- Mirnov diagnostics: channels from 01 to 24, with nomeclature `BBMRNVN##.signal`.

- SXR diagnostics: channels from  01 to 20, with nomeclature `SOFTXR0##.signal`.

- $H_\alpha$ diagnostics: one channel, named `HALFAREF0.signal`.

For the channels investigated, each signal contains 100,000 points over a total time interval of approximately 200 ms. The stored signals are given in voltage units (V). The time step is approximately 1.9989 ms, corresponding to a sampling frequency of approximately 500.3 Hz.

By taking the channels `BBMRNVN01.signal`, `SOFTXR001.signal`, and `HALFAREF0.signal`, we can plot graphs of signal x time for each one of them, whose code is located in the [mdsplus_first_acess.ipynb](../src/mdsplus_first_acess.ipynb) file. Then, we have for the Mirnov Coil N° 1:

<img width="790" height="440" alt="image" src="https://github.com/user-attachments/assets/c6d41cca-4b26-4e62-9bef-029b05139d35" />

For the SXR signal N° 1

<img width="790" height="440" alt="image" src="https://github.com/user-attachments/assets/88a5abfb-236a-43a7-9809-d4ce2c1f8e55" />

And for the reference $H_\alpha$

<img width="790" height="440" alt="image" src="https://github.com/user-attachments/assets/0307ff70-ee59-43ae-9fb8-15cb6696749a" />


