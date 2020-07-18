package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ISpeed;
import www.google.com.digitalbuildings._0_0_1.subfields.IFan;
import www.google.com.digitalbuildings._0_0_1.subfields.ISupply;
import www.google.com.digitalbuildings._0_0_1.subfields.IFrequency;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface ISupply_fan_speed_frequency_sensor_2 extends IField{

	public IRI iri();

    public void addComposedOfFan (IFan parameter);

	public Set<IFan> getComposedOfFan();

    public void addComposedOfFrequency (IFrequency parameter);

	public Set<IFrequency> getComposedOfFrequency();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfSpeed (ISpeed parameter);

	public Set<ISpeed> getComposedOfSpeed();

    public void addComposedOfSupply (ISupply parameter);

	public Set<ISupply> getComposedOfSupply();

}