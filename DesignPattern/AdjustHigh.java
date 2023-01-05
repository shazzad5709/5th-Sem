public class AdjustHigh implements AdjustColorIntensity{
    protected String tonerSavingLevel;
    protected String colorIntensity;
    @Override
    public void adjustColorIntensity() {

        if(tonerSavingLevel == "high"){
            colorIntensity="highly reduced";
        }
    }
}
