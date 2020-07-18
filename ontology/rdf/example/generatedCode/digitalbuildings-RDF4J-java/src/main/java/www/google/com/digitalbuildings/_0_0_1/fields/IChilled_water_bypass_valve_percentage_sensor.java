package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IChilled;
import www.google.com.digitalbuildings._0_0_1.subfields.IWater;
import www.google.com.digitalbuildings._0_0_1.subfields.IBypass;
import www.google.com.digitalbuildings._0_0_1.subfields.IPercentage;
import www.google.com.digitalbuildings._0_0_1.subfields.IValve;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IChilled_water_bypass_valve_percentage_sensor extends IField{

	public IRI iri();

    public void addComposedOfBypass (IBypass parameter);

	public Set<IBypass> getComposedOfBypass();

    public void addComposedOfChilled (IChilled parameter);

	public Set<IChilled> getComposedOfChilled();

    public void addComposedOfPercentage (IPercentage parameter);

	public Set<IPercentage> getComposedOfPercentage();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfValve (IValve parameter);

	public Set<IValve> getComposedOfValve();

    public void addComposedOfWater (IWater parameter);

	public Set<IWater> getComposedOfWater();

}