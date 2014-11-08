import Pmf
import relay
import myplot

def runner_pmf(pmf, name, runner_speed):
    """
    Given the pmf of actual speed values of runners, returns a pmf
    of the speed distribution as perceived by a runner. The probability relative 
    to a runner will be proportional to the difference between the runner's speed 
    and the others. 

    Args:
    pmf - the distribution of actual speeds
    runner_speed - the speed of a runner

    Returns:
    A pmf that represents the speed distribution as perceived by a runner 
    """
    if runner_speed <= 0:
        return
    bias_pmf = pmf.Copy(name=name)
    for val in bias_pmf.Values():
        speed_diff = abs(val - runner_speed) 
        bias_pmf.Mult(val, speed_diff)
    bias_pmf.Normalize()
    return bias_pmf

def main():
    relay_results = relay.ReadResults()
    relay_speeds = relay.GetSpeeds(relay_results)
    speed_pmf = Pmf.MakePmfFromList(relay_speeds, "actual speeds")
    RUNNER_SPEED = 8 # Speed of a runner in mph
    runner_bias_pmf = runner_pmf(speed_pmf, "perceived speeds", RUNNER_SPEED)
    myplot.Pmfs([speed_pmf, runner_bias_pmf])
    myplot.Show(title="Pmf of running speeds", 
        xlabel="Speed in mph",
        ylabel="Probability")

if __name__ == "__main__":
     main()
