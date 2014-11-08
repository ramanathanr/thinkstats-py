import Cdf
import myplot
import relay

def main():
    relay_records = relay.ReadResults()
    speedlist = relay.GetSpeeds(relay_records)
    cdf_speeds = Cdf.MakeCdfFromList(speedlist)
    myplot.Cdf(cdf_speeds)
    myplot.Show(title="Cdf of running speeds",
            xlabel="speed in mph",
            ylabel="cdf(speed)")
    
if __name__ == "__main__":
    main()

    
