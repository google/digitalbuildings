package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ICurrent;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface ICurrent_sensor extends IField{

	public IRI iri();

    public void addComposedOfCurrent (ICurrent parameter);

	public Set<ICurrent> getComposedOfCurrent();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}