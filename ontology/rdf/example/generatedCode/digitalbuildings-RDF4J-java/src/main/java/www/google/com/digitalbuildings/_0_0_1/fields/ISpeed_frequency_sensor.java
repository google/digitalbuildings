package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ISpeed;
import www.google.com.digitalbuildings._0_0_1.subfields.IFrequency;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface ISpeed_frequency_sensor extends IField{

	public IRI iri();

    public void addComposedOfFrequency (IFrequency parameter);

	public Set<IFrequency> getComposedOfFrequency();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfSpeed (ISpeed parameter);

	public Set<ISpeed> getComposedOfSpeed();

}