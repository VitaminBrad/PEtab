import pandas as pd
import group_plot


def plot_simulationdata(DataFilePath, ConditionFilePath, ax,
                        legend='simulation'):
    '''
    plot simulation data grouped by variable ID

    Parameters:
    ----------

    DataFilePath: string, file path of measurement data
    ConditionFilePath: string, file path of condition file
    ax: axis of figures on top of which the simulation data will be plotted
    legend: sting, legend for plotted data

    Return:
    ----------

    axis: axis of figures
    '''

    # import measurement data
    simulate_data = pd.DataFrame.from_csv(
        DataFilePath, sep="\t", index_col=None)
    # import experimental condition
    experimental_condition = pd.DataFrame.from_csv(
        ConditionFilePath, sep="\t")

    ax = group_plot.group_plot(simulate_data, experimental_condition,
                               axis=ax, legend=legend)
    return ax
