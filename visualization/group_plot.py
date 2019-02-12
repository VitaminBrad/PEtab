import numpy as np
import matplotlib.pyplot as plt

def group_plot(data_frame, condition, axis=None):
    experimentId = np.array(data_frame.experimentId)
    observableId = np.array(data_frame.observableId)
    measurement = np.array(data_frame.measurement)
    simulationCon = np.array(data_frame.simulationConditionId)
    time = np.array(data_frame.time)
    independentVarId = np.array(data_frame.independentVariableId)

    # get unique experiment ID
    uni_experimentId = np.unique(experimentId)

    # one figure for each experiment ID
    plot_axis = np.empty(len(uni_experimentId), dtype=object)

    # for each unique experiment ID get observable ID, independent variable
    # ID and measurements
    for i_uniexp, val_uniexp in enumerate(uni_experimentId):
        ind_uniexp = np.where(experimentId == val_uniexp)[0]
        observableId_uniexp = observableId[ind_uniexp]
        indvarId_uniexp = independentVarId[ind_uniexp]
        measurement_uniexp = measurement[ind_uniexp]
        time_uniexp = time[ind_uniexp]
        simcon_uniexp = simulationCon[ind_uniexp]

        uni_obs = np.unique(observableId_uniexp)

        # each sub plot for one observable ID
        if axis is None:
            num_subplot = len(uni_obs)
            num_row = np.round(np.sqrt(num_subplot))
            num_col = np.ceil(num_subplot / num_row)
            fig, ax = plt.subplots(int(num_row), int(num_col))
        else:
            ax = axis[i_uniexp]
            if hasattr(ax, 'size'):
                num_subplot = ax.size
            else:
                num_subplot = 1

        # check if it is time response or dose response
        indvarId_uniexp = indvarId_uniexp[0]
        for i_uniobs, val_uniobs in enumerate(uni_obs):
            ind_uniobs = np.where(observableId_uniexp == val_uniobs)[0]
            measurement_uniobs = measurement_uniexp[ind_uniobs]
            # check which values should be the xaxis
            if (indvarId_uniexp == 'time'):
                xaxis = time_uniexp[ind_uniobs]
                xaxis_label = 'time'

            else:
                simcon_uniobs = simcon_uniexp[ind_uniobs]
                dose = condition[indvarId_uniexp]
                xaxis = dose[simcon_uniobs]
                xaxis_label = indvarId_uniexp

            if (num_subplot == 1):
                ax.plot(xaxis, measurement_uniobs, 'x')
                ax.set_xlabel(xaxis_label)
                ax.set_ylabel('measurement')
            elif (num_subplot == 2):
                ax[i_uniobs].plot(xaxis, measurement_uniobs, 'x')
                ax[i_uniobs].set_xlabel(xaxis_label)
                ax[i_uniobs].set_ylabel('measurement')
            else:
                axx = np.ceil(i_uniobs / num_col) - 1
                axy = i_uniobs - axx * num_col - 1
                ax[axx, axy].plot(xaxis, measurement_uniobs, 'x')
                ax[axx, axy].set_xlabel(xaxis_label)
                ax[axx, axy].set_ylabel('measurement')

        fig.suptitle(val_uniexp)

        plot_axis[i_uniexp] = ax

    return plot_axis